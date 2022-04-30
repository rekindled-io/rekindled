import { Plugin } from "@nuxt/types";
import { UserService } from "~/modules/user/UserService";
import { GameService } from "~/modules/game/GameService";
import { PlatformService } from "~/modules/platform/PlatformService";

export interface Services {
  user: UserService;
  game: GameService;
  platform: PlatformService;
}

declare module "vue/types/vue" {
  interface Vue {
    readonly $services: Services;
  }
}

const servicePlugin: Plugin = ({ app: { $axios } }, inject) => {
  const services: Services = {
    user: new UserService($axios),
    game: new GameService($axios),
    platform: new PlatformService($axios),
  };

  inject("services", services);
};

export default servicePlugin;