<template>
  <div class="message-type__file">
    <a :href="$http.download(message.message)">[文件]{{ message.message }}</a>
  </div>
</template>

<script>
import './../../../static/iconfont/iconfont.css'
export default {
  props: ['message'],
}
</script>
