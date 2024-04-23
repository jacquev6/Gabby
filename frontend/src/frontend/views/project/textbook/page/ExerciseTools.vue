<script setup>
import { BLabeledInput, BButton } from '../../../../components/opinion/bootstrap'
</script>

<template>
  <h1>{{ $t('tools') }}</h1>
  <hr/>
  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin feugiat ante id iaculis malesuada. Cras viverra est vel purus luctus congue. Phasellus magna massa, placerat eget facilisis sed, mattis sit amet sapien.</p>
  <hr/>
  <p>Sed metus purus, dapibus ut hendrerit a, tempus non risus. Quisque congue nisl sit amet erat placerat, quis pulvinar neque pulvinar. Proin eu rutrum ipsum. Fusce risus sapien, pharetra imperdiet metus at, elementum tincidunt odio.</p>
  <hr/>
  <div @mousedown="e => e.stopPropagation()" @touchstart="e => e.stopPropagation()" style="cursor: initial;">
    <BLabeledInput :label="$t('replace')"/>
    <BLabeledInput :label="$t('replaceWith')"/>
    <p><BButton primary data-cy="apply-replace">{{ $t('apply') }}</BButton></p>
  </div>
  <hr/>
</template>
