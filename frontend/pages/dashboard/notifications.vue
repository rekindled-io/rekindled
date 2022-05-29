<template>
  <div>
    <div v-if="$fetchState.pending">
      <Loading />
    </div>
    <div class="mx-auto my-4 text-center font-semibold py-2" v-else-if="!this.notifications.count">
      <span class="text-xl font-semibold">You have no notifications.</span>
    </div>
    <table v-else class="min-w-full mt-5">
      <thead class="border-t-2 border-b-2 bg-gray-100 text-gray-600 text-xs font-medium uppercase">
        <tr>
          <th class="py-4 text-center">Subject</th>
          <th class="py-4 text-center">Message</th>
          <th class="py-4 text-center">When</th>
          <th class="py-4 text-center">Actions</th>
        </tr>
      </thead>
      <tbody class="text-sm font-normal text-gray-700">
        <tr
          v-for="notification in notifications.results"
          :key="`${notification}`"
          class="hover:bg-gray-100"
          :class="[notification.unread ? 'bg-white border-l-4 border-yellow-500' : 'bg-gray-50']"
        >
          <td class="px-6 py-4 border-b border-1">
            <div class="flex align-items-center box-border">
              <div class="text-sm" :class="[notification.unread ? 'font-bold ' : 'text-gray-500']">
                <span class="font-bold">{{ notification.sender.user }}</span> from
                <span class="font-bold">
                  {{ notification.sender.game_and_platform.game_name }} ({{
                    notification.sender.game_and_platform.platform_name
                  }})</span
                >
                wants to kindle with <span class="font-bold">{{ notification.recipient.user }}</span> from
                <span class="font-bold">
                  {{ notification.recipient.game_and_platform.game_name }} ({{
                    notification.recipient.game_and_platform.platform_name
                  }})</span
                >
              </div>
            </div>
          </td>
          <td class="text-center border-b border-1">
            <div v-if="notification.message">
              {{ notification.message | truncate(32) }}
            </div>
            <div v-else>
              <span class="italic">No message.</span>
            </div>
          </td>
          <td class="text-center border-b border-1" :class="[notification.unread ? 'font-bold' : '']">
            {{ notification.timestamp }}
          </td>
          <td class="text-center border-b border-1">
            <a class="text-gray-500 ml-2 hover:bg-gray-200 px-3 py-2 rounded cursor-pointer">
              <NuxtLink to="/user/asdfgh">
                <span class="text-base">view</span>
              </NuxtLink>
            </a>
            <a class="text-red-500 ml-2 hover:bg-gray-200 px-3 py-2 rounded cursor-pointer">
              <span class="text-base">delete</span>
            </a>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
<script>
import '@/plugins/truncate'
export default {
  data() {
    return {
      notifications: []
    }
  },
  async fetch() {
    this.notifications = await this.$axios.$get(`/notifications/`)
  }
}
</script>
