<script lang="ts">

const listFormats = [
  () => {
    // "a. b. c.", "A) B) C)", etc.
    let firstCall = true
    let next: number | null = null
    let separator: string | null = null
    return {
      startsNextItem(line: TextItem[]) {
        if (firstCall) {
          for (const nex of ['a', 'A']) {
            if (line[0].str.charCodeAt(0) === nex.charCodeAt(0)) {
              next = nex.charCodeAt(0)
              break
            }
          }

          for (const sep of ['.', ')']) {
            if (line[0].str[1] === sep) {
              separator = sep
              break
            }
          }

          firstCall = false
        }

        if (
          next !== null && line[0].str.charCodeAt(0) === next
          && separator !== null && line[0].str[1] === separator
        ) {
          ++next
          return true
        } else {
          return false
        }
      },
    }
  },
  () => {
    // "1. 2. 3.", "1) 2) 3)", etc.
    let firstCall = true
    let separator: string | null = null
    let next = 1
    return {
      startsNextItem(line: TextItem[]) {
        if (firstCall) {
          for (const sep of ['.', ')']) {
            if (line[0].str[1/* Because the number has to be '1', which is one character wide */] === sep) {
              separator = sep
              break
            }
          }

          firstCall = false
        }

        if (parseInt(line[0].str) === next && separator !== null && line[0].str.slice(next.toString().length, next.toString().length + 1) === separator) {
          ++next
          return true
        } else {
          return false
        }
      },
    }
  },
  () => {
    // "◆", "■", etc.
    let firstCall = true
    let bullet: string | null = null
    return {
      startsNextItem(line: TextItem[]) {
        if (firstCall) {
          for (const bul of ['◆', '■']) {
            if (line[0].str[0] === bul) {
              bullet = bul
              break
            }
          }

          firstCall = false
        }

        return line[0].str[0] === bullet
      },
    }
  },
  // WARNING: keep the set of list formats supported here consistent with what's supported by '_Adapter.split_list_header' in 'adaptation.py'.
]

export interface SelectedText {
  withoutLineEnds: string
  withAllLineEnds: string
  withoutListsDetection: string
}

function textFromItems(items: TextItem[]): SelectedText {
  // Coordinates start from the lower left corner of the page, growing upwards and to the right.
  const left = items.reduce((acc, item) => Math.min(acc, item.left), Infinity)
  const right = items.reduce((acc, item) => Math.max(acc, item.right), -Infinity)
  const width = right - left
  const top = items.reduce((acc, item) => Math.max(acc, item.top), -Infinity)
  const bottom = items.reduce((acc, item) => Math.min(acc, item.bottom), Infinity)
  // const height = top - bottom

  const lines: TextItem[][] = [[]]
  for (const item of items) {
    console.assert(item.left >= left)
    console.assert(item.right <= right)
    console.assert(item.top <= top)
    console.assert(item.bottom >= bottom)

    if (item.str.trim() !== '') {
      let currentLine = lines[lines.length - 1]
      if (currentLine.length === 0) {
        currentLine.push(item)
      } else {
        const previousItem = currentLine[currentLine.length - 1]
        if (Math.abs(previousItem.bottom - item.bottom) > 0.5 * previousItem.height) {
          lines.push([item])
        } else {
          currentLine.push(item)
        }
      }
    }
  }
  // 'TextItems' and not always in reading order (increasing abscissa) => sort them
  // Side note: we'll probably hit a case where they are not even in increasing ordinate order,
  // which will result in mangled extraction. We'll tackle this when we have a concrete example.
  for (const line of lines) {
    line.sort((a, b) => a.left - b.left)
  }

  function textFromLine(line: TextItem[]) {
    if (line.length === 0) {
      return ''
    } else {
      var text = line[0].str
      for (let i = 1; i !== line.length; ++i) {
        const previousItem = line[i - 1]
        const item = line[i]
        if (item.left - previousItem.right > 0.001 * width) {
          text += ' '
        }
        text += item.str
      }
      // Ellipsis is a confusing character; people don't know how to type it.
      // It's often used as the placeholder for missing text, so needs to be typed in some fields
      // like "placeholder for free text" or the "placeholder to fill" for MCQs.
      // So we replace the ellipsis character with three dots, that people definitely know how to type.
      text = text.replaceAll('…', '...')
      return text
    }
  }

  if (lines[0].length === 0) {
    return {withoutLineEnds: '', withAllLineEnds: '', withoutListsDetection: ''}
  } else {
    function lineLooksJustified(line: TextItem[]) {
      return Math.abs(line[line.length - 1].right - right) < 0.02 * width
    }

    let withoutListsDetection = ''
    if (lines.filter(lineLooksJustified).length >= lines.length / 2) {
      // Justified text: shorter lines end with a line break
      let text = ''
      for (const line of lines) {
        text += textFromLine(line)
        if (lineLooksJustified(line)) {
          text += ' '
        } else {
          text += '\n'
        }
      }
      withoutListsDetection = text.trimEnd()
    } else {
      // General case: we add a line break if the spacing before this line is larger than the spacing before previous line
      if (lines.length === 1) {
        withoutListsDetection = textFromLine(lines[0])
      } else {
        console.assert(lines.length >= 2)

        const lineSpacings = lines.slice(1).map((line, i) => lines[i][0].bottom - line[0].bottom)
        lineSpacings.sort((a, b) => a - b)
        const standardLineSpacing = lineSpacings[Math.floor(lineSpacings.length / 2)]

        let text = textFromLine(lines[0]) + ' ' + textFromLine(lines[1])
        for (let i = 2; i !== lines.length; ++i) {
          if (lines[i - 1][0].bottom - lines[i][0].bottom >= 1.1 * standardLineSpacing) {
            text += '\n'
          } else {
            text += ' '
          }
          text += textFromLine(lines[i])
        }
        withoutListsDetection = text
      }
    }

    const matchingListFormats = listFormats.filter(listFormat => {
      const format = listFormat()
      // A list format matches the text if the first line starts a new list item...
      if (format.startsNextItem(lines[0])) {
        for (const line of lines.slice(1)) {
          // ... and some other line starts another list item.
          if (format.startsNextItem(line)) {
            return true
          }
        }
      }
      return false
    })

    let withoutLineEnds = ''
    if (matchingListFormats.length >= 1) {
      // List: each list item ends with a line break
      console.assert(lines.length >= 2)
      const listFormat = matchingListFormats[0]()

      const firstLineOk = listFormat.startsNextItem(lines[0])  // May have side effects in the 'listFormat'
      console.assert(firstLineOk)
      let text = textFromLine(lines[0])
      for (const line of lines.slice(1)) {
        if (listFormat.startsNextItem(line)) {
          text += '\n'
        } else {
          text += ' '
        }
        text += textFromLine(line)
      }
      withoutLineEnds = text.trimEnd()
    } else {
      withoutLineEnds = withoutListsDetection
    }

    const withAllLineEnds = lines.map(textFromLine).join('\n')

    return {
      withoutLineEnds: withoutLineEnds + '\n',
      withAllLineEnds: withAllLineEnds + '\n',
      withoutListsDetection: withoutListsDetection + '\n',
    }
  }
}
</script>

<script setup lang="ts">
import { ref, computed, watch } from 'vue'

import type { Point, Rectangle } from './RectanglesHighlighter.vue'


export interface TextItem {
  left: number,
  right: number,
  width: number,
  top: number,
  bottom: number,
  height: number,
  str: string,
}

// WARNING: this component doesn't handle well when its props are changed after it's mounted.
const props = defineProps<{
  width: number,
  height: number,
  transform: number[],
  textContent: TextItem[],
}>()

const emit = defineEmits<{
  textSelected: [text: SelectedText, point: {clientX: number, clientY: number}, rectangle: Rectangle],
}>()

const canvas = ref<HTMLCanvasElement | null>(null)
const context = computed(() => canvas.value?.getContext('2d') ?? null)

watch([props, context], () => {
  console.assert(canvas.value !== null)
  console.assert(context.value !== null)

  canvas.value.width = props.width
  canvas.value.height = props.height

  context.value.setTransform(props.transform[0], props.transform[1], props.transform[2], props.transform[3], props.transform[4], props.transform[5])
})

var startPoint: Point | null = null

function pointerdown(event: any/* @todo Type */) {
  console.assert(canvas.value !== null)

  startPoint = makeCanvasPoint(event)
  canvas.value.setPointerCapture(event.pointerId)
}

function pointermove(event: any/* @todo Type */) {
  console.assert(context.value !== null)

  if (startPoint !== null) {
    clearCanvas()

    const r = selectionRectangle(startPoint, makeCanvasPoint(event))

    context.value.save()
    context.value.beginPath()
    for (var item of props.textContent.filter(r.contains)) {
      context.value.rect(item.left, item.bottom, item.width, item.height)
    }
    context.value.fillStyle = 'rgba(255, 255, 0, 0.5)'
    context.value.strokeStyle = 'rgba(255, 128, 0, 0.5)'
    context.value.fill()
    context.value.stroke()
    context.value.restore()

    context.value.beginPath()
    context.value.rect(r.minX, r.minY, r.maxX - r.minX, r.maxY - r.minY)
    context.value.stroke()
  }
}

function pointerup(event: any/* @todo Type */) {
  console.assert(canvas.value !== null)

  canvas.value.releasePointerCapture(event.pointerId)
  if (startPoint !== null) {
    clearCanvas()

    const stopPoint = makeCanvasPoint(event)
    const r = selectionRectangle(startPoint, stopPoint)

    const text = textFromItems(props.textContent.filter(r.contains))

    if (text.withoutLineEnds !== '') {
      emit(
        'textSelected',
        text,
        {clientX: event.clientX, clientY: event.clientY},
        {start: {x: startPoint.x, y: startPoint.y}, stop: {x: stopPoint.x, y: stopPoint.y}},
      )
    }

    startPoint = null
  }
}

function makeCanvasPoint(event: any/* @todo Type */) {
  console.assert(canvas.value !== null)
  console.assert(context.value !== null)

  const rect = canvas.value.getBoundingClientRect()
  const scaleX = canvas.value.width / rect.width
  const scaleY = canvas.value.height / rect.height
  return context.value.getTransform().inverse().transformPoint(
    new DOMPoint((event.clientX - rect.left) * scaleX, (event.clientY - rect.top) * scaleY)
  )
}

function selectionRectangle(startPoint: Point, endPoint: Point) {
  const minX = Math.min(startPoint.x, endPoint.x)
  const maxX = Math.max(startPoint.x, endPoint.x)
  const minY = Math.min(startPoint.y, endPoint.y)
  const maxY = Math.max(startPoint.y, endPoint.y)

  return {
    minX, maxX, minY, maxY,
    contains(item: TextItem) {
      return (
        item.left >= minX && item.right <= maxX
        && item.bottom >= minY && item.top <= maxY
      )
    },
  }
}

function clearCanvas() {
  console.assert(canvas.value !== null)
  console.assert(context.value !== null)

  context.value.save()
  context.value.setTransform(1, 0, 0, 1, 0, 0)
  context.value.clearRect(0, 0, canvas.value.width, canvas.value.height)
  context.value.restore()
}
</script>

<template>
  <canvas ref="canvas" @pointerdown="pointerdown" @pointermove="pointermove" @pointerup="pointerup"></canvas>
</template>
