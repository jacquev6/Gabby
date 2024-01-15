<template>
  <div class="container-fluid">
    <h1>Gabby</h1>
    <div class="row">
      <div class="col">
        <h2>PDF</h2>
        <div id="canvas-container" style="background-color: blue;">
          <canvas id="pdf-canvas"></canvas>
          <canvas id="ui-canvas" @mousedown="mousedown" @mousemove="mousemove" @mouseup="mouseup"></canvas>
        </div>
      </div>
      <div class="col">
        <h2>Form</h2>
        <p>Start point: {{ startPoint }}</p>
        <p>End point: {{ endPoint }}</p>
        <p>Last selected text: {{ lastSelectedText }}</p>
      </div>
    </div>
  </div>
</template>

<script async>
import { ref } from 'vue'

// @todo Upgrade pdfjs-dist. 2.4.456 is OK but I couldn't get more recent versions to work.
// (Some versions result in pdfjs being undefined; others juste fail to import.)
import pdfjs from 'pdfjs-dist/build/pdf';
pdfjs.GlobalWorkerOptions.workerSrc = `https://cdn.jsdelivr.net/npm/pdfjs-dist@${pdfjs.version}/build/pdf.worker.min.js`

var pdf = await pdfjs.getDocument('test.pdf').promise
var page = await pdf.getPage(1)
var textContent = await page.getTextContent()

export default {
  setup() {
    return {
      lastSelectedText: ref("None"),
      startPoint: ref(null),
      endPoint: ref(null),
    }
  },
  async mounted() {
    var scale = 1.0
    var viewport = page.getViewport({scale: scale})
    console.log(viewport)
    document.getElementById('canvas-container').style.width = viewport.width + 'px'
    document.getElementById('canvas-container').style.height = viewport.height + 'px'
    var pdfCanvas = document.getElementById('pdf-canvas')
    var pdfContext = pdfCanvas.getContext('2d')
    pdfCanvas.height = viewport.height
    pdfCanvas.width = viewport.width
    var renderContext = {
      canvasContext: pdfContext,
      viewport: viewport
    }
    await page.render(renderContext).promise

    this.uiCanvas = document.getElementById('ui-canvas')
    this.uiCanvas.height = viewport.height
    this.uiCanvas.width = viewport.width
    this.uiContext = this.uiCanvas.getContext('2d')
    this.uiContext.setTransform(viewport.transform[0], viewport.transform[1], viewport.transform[2], viewport.transform[3], viewport.transform[4], viewport.transform[5])
  },
  methods: {
    mousedown(e) {
      this.startPoint = this.uiContext.getTransform().inverse().transformPoint(new DOMPoint(e.layerX, e.layerY))
    },
    mousemove(e) {
      if (this.startPoint !== null) {
        this.uiContext.save()
        this.uiContext.setTransform(1, 0, 0, 1, 0, 0)
        this.uiContext.clearRect(0, 0, this.uiCanvas.width, this.uiCanvas.height)
        this.uiContext.restore()

        this.endPoint = this.uiContext.getTransform().inverse().transformPoint(new DOMPoint(e.layerX, e.layerY))

        var minX = Math.min(this.startPoint.x, this.endPoint.x)
        var maxX = Math.max(this.startPoint.x, this.endPoint.x)
        var minY = Math.min(this.startPoint.y, this.endPoint.y)
        var maxY = Math.max(this.startPoint.y, this.endPoint.y)

        this.uiContext.beginPath()
        for (var item of textContent.items) {
          var itemLeft = item.transform[4]
          var itemRight = item.transform[4] + item.width
          var itemTop = item.transform[5]
          var itemBottom = item.transform[5] + item.height
          if (
            itemLeft >= minX && itemRight <= maxX
            && itemTop >= minY && itemBottom <= maxY
          ) {
            this.uiContext.rect(itemLeft, itemTop, item.width, item.height)
          }
        }
        this.uiContext.stroke()

        this.uiContext.beginPath()
        this.uiContext.rect(minX, minY, maxX - minX, maxY - minY)
        this.uiContext.stroke()
      }
    },
    mouseup(e) {
      if (this.startPoint !== null) {
        this.endPoint = this.uiContext.getTransform().inverse().transformPoint(new DOMPoint(e.layerX, e.layerY))

        var minX = Math.min(this.startPoint.x, this.endPoint.x)
        var maxX = Math.max(this.startPoint.x, this.endPoint.x)
        var minY = Math.min(this.startPoint.y, this.endPoint.y)
        var maxY = Math.max(this.startPoint.y, this.endPoint.y)

        this.lastSelectedText = ""
        for (var item of textContent.items) {
          var itemLeft = item.transform[4]
          var itemRight = item.transform[4] + item.width
          var itemTop = item.transform[5]
          var itemBottom = item.transform[5] + item.height
          if (
            itemLeft >= minX && itemRight <= maxX
            && itemTop >= minY && itemBottom <= maxY
          ) {
            this.lastSelectedText += ' ' + item.str
          }
        }

        this.uiContext.save()
        this.uiContext.setTransform(1, 0, 0, 1, 0, 0)
        this.uiContext.clearRect(0, 0, this.uiCanvas.width, this.uiCanvas.height)
        this.uiContext.restore()
        this.startPoint = null
        this.endPoint = null
      }
    },
  },
};
</script>

<style>
#canvas-container {
  position: relative;
  float: left;
  border: 1px black solid;
}
#pdf-canvas { position: absolute; left: 0; top: 0; z-index: 0; }
#ui-canvas { position: absolute; left: 0; top: 0; z-index: 1; }
</style>
