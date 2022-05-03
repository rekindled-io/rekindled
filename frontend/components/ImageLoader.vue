<template>
  <div>
    <img v-if="imageLoaded" :src="this.image.src" :class="imageClass" />
    <div v-else class="h-48 w-48">
      <Loading />
    </div>
  </div>
</template>

<script>
export default {
  props: {
    imageSource: {
      type: String,
      required: true
    },
    imageClass: {
      type: String,
      required: false,
      default: ''
    }
  },
  data() {
    return {
      imageLoaded: false,
      image: new Image()
    };
  },
  mounted() {
    this.$nextTick(() => {
      this.fetchImage();
    });
  },
  methods: {
    fetchImage() {
      this.image.onload = this.imageOnLoad;
      this.imageLoaded = false;
      this.image.src = this.imageSource;
    },
    imageOnLoad() {
      this.imageLoaded = true;
    }
  }
};
</script>
