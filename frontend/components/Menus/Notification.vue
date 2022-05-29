<template>
  <MenusBase>
    <template #head>
      <div class="cursor-pointer p-relative">
        <Icon class="text-gray-200 rounded-lg w-7 h-7" name="bell" />
        <span class="absolute top-0 right-0 -mt-2 -mr-2 text-white">
          <Pill :name="unreadNotifications" v-if="unreadNotifications > 0" />
        </span>
      </div>
    </template>
    <template #body>
      <div class="px-4 py-2 font-bold text-gray-700">Message Notifications</div>
      <div class="w-full border-t border-gray-300"></div>
      <Loading v-if="$fetchState.pending" />
      <div v-else-if="!notifications.count" class="p-4">You have no notifications.</div>
      <div v-else>
        <div
          class="flex px-2 my-2 rounded-md"
          v-for="(notification, index) in notifications.results"
          :key="`#${index}-${notification.timestamp}`"
        >
          <Nuxt-Link
            to="/dashboard/notifications/"
            :class="[notification.unread ? 'border-l-4 border-blue-500 bg-gray-50' : '']"
            class="block px-4 py-3 text-sm text-gray-700 rounded-md hover:bg-yellow-300 hover:text-gray-800"
          >
            <div class="flex items-center justify-between py-1">
              <span class="font-bold">New kindle request!</span>
              <span class="text-xs font-bold text-gray-600">{{ notification.timestamp }}</span>
            </div>
            <div>
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
          </Nuxt-Link>
          <hr />
        </div>
      </div>
      <Nuxt-Link
        to="/dashboard/notifications/"
        class="block px-4 py-3 text-sm font-bold text-center text-gray-900 bg-yellow-400"
      >
        View All Notifications
      </Nuxt-Link>
    </template>
  </MenusBase>
</template>

<script lang="ts">
import Vue from 'vue';
import { mapGetters } from 'vuex';
import { NotificationList } from '~/modules/notification/Notification';

export default Vue.extend({
  data() {
    return {
      notifications: {} as NotificationList
    };
  },

  computed: {
    ...mapGetters('auth', ['isAuthenticated']),
    unreadNotifications(): number | undefined {
      if (this.notifications!.count && this.isAuthenticated) {
        return this.notifications.results?.filter((n: any) => {
          return n.unread;
        }).length;
      }
    }
  },

  async fetch() {
    if (this.isAuthenticated) {
      this.notifications = await this.$services.notification.list();
    }
  }
});
</script>
