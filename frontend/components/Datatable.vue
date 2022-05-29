<template>
  <table class="table w-full my-2">
    <thead class="text-xs text-gray-600 bg-gray-100 border-t-2 border-b-1">
      <tr>
        <th class="py-4">#</th>
        <th class="py-4 text-left" v-for="(head, index) in keys" :key="index">{{ head | capitalise }}</th>
      </tr>
    </thead>
    <tbody class="text-sm font-normal text-gray-700">
      <tr
        v-for="(row, index) in data"
        :key="`row-#${index}`"
        :class="[index + 1 != data.length ? 'border-b' : '']"
        class="hover:bg-gray-50"
      >
        <td class="py-4 font-semibold text-center">{{ total - index }}</td>
        <td v-for="(col, colIndex) in keys" :key="`col-#${colIndex}`">
          <slot :item="row.toDataTable()[col]" :name="col">
            {{ row.toDataTable()[col] }}
          </slot>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script lang="ts">
import Vue from 'vue';

export default Vue.extend({
  props: {
    headers: {
      type: Array,
      required: false
    },
    data: {
      type: Array,
      required: true
    },
    keys: {
      type: Array,
      required: true
    },
    total: {
      type: Number,
      required: true
    }
  }
});
</script>
