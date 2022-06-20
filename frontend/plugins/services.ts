import { Plugin } from '@nuxt/types';
import { UserService } from '~/modules/user/UserService';
import { GameService } from '~/modules/game/GameService';
import { PlatformService } from '~/modules/platform/PlatformService';
import { HandleService } from '~/modules/handle/HandleService';
import { NotificationService } from '~/modules/notification/NotificationService';
import { DirectKindleService } from '~/modules/kindle/KindleService';

export interface Services {
  user: UserService;
  game: GameService;
  platform: PlatformService;
  handle: HandleService;
  notification: NotificationService;
  directKindle: DirectKindleService;
}

declare module 'vue/types/vue' {
  interface Vue {
    readonly $services: Services;
  }
}

declare module '@nuxt/types' {
  interface Context {
    readonly $services: Services;
  }
}

const servicePlugin: Plugin = ({ app: { $axios } }, inject) => {
  const services: Services = {
    user: new UserService($axios),
    game: new GameService($axios),
    platform: new PlatformService($axios),
    handle: new HandleService($axios),
    notification: new NotificationService($axios),
    directKindle: new DirectKindleService($axios)
  };

  inject('services', services);
};

export default servicePlugin;
