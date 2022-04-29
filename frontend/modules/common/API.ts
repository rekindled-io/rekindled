import { NuxtAxiosInstance } from "@nuxtjs/axios";

export default class APIService {
  client: NuxtAxiosInstance;

  constructor($axios: NuxtAxiosInstance) {
    this.client = $axios;
  }

  get(path: string) {
    return this.client.get(path);
  }

  post(path: string, payload: Object) {
    return this.client.post(path, payload);
  }
}
