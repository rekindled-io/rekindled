<template>
  <div>
    <div v-if="$fetchState.pending">
      <Loading />
    </div>
    <div class="py-2 mx-auto my-4 font-semibold text-center" v-else-if="!this.notifications.count">
      <span class="text-xl font-semibold">You have no notifications.</span>
    </div>
    <table v-else class="min-w-full mt-5">
      <thead class="text-xs font-medium text-gray-600 uppercase bg-gray-100 border-t-2 border-b-2">
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
            <div class="box-border flex align-items-center">
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
            <a class="px-3 py-2 ml-2 text-gray-500 rounded cursor-pointer hover:bg-gray-200">
              <NuxtLink to="/user/asdfgh">
                <span class="text-base">view</span>
              </NuxtLink>
            </a>
            <a class="px-3 py-2 ml-2 text-red-500 rounded cursor-pointer hover:bg-gray-200">
              <span class="text-base">delete</span>
            </a>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
<script>
export default {
  data() {
    return {
      notifications: []
    };
  },
  async fetch() {
    this.notifications = await this.$axios.$get(`/notifications/`);
  }
};
</script>
