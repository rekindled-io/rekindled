<template>
  <ModalsBase title="Confirmation" :open="open" v-on="$listeners">
    <template #body>
      <div class="my-5 text-center w-full">
        {{ message }}
      </div>
      <hr />
      <div class="flex justify-center mt-4" role="group">
        <button
          @click="$emit('action')"
          class="w-full rounded-l-lg bg-red-600 py-2 text-white font-bold hover:bg-red-700 focus:outline-none focus:border-red-800 focus:shadow-outline-red transition ease-in-out duration-100"
        >
          {{ actionLabel }}
        </button>
        <button
          @click="$emit('cancel')"
          class="w-full rounded-r-lg bg-gray-200 text-gray-600 hover:bg-gray-300 focus:outline-none focus:border-red-700 transition ease-in-out duration-150"
        >
          {{ cancelLabel }}
        </button>
      </div>
    </template>
  </ModalsBase>
</template>

<script>
export default {
  name: 'ActionModal',
  props: {
    open: {
      type: Boolean,
      required: true
    },
    message: {
      type: String,
      required: false
    },
    actionLabel: {
      type: String,
      required: false,
      default: 'Ok'
    },
    cancelLabel: {
      type: String,
      required: false,
      default: 'Cancel'
    }
  }
};
</script>
