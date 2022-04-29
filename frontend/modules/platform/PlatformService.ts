import APIService from "../common/API";
import { Platform } from "./Platform";

export class PlatformService extends APIService {
  private url = "games/";

  async list(): Promise<Platform> {
    const response = await this.client.get(this.url);
    return new Platform(response.data);
  }
}
