import APIService from "../common/API";
import { HandleList } from "./Handle";

export class HandleService extends APIService {
  private url = "handles/";

  async list(query?: string): Promise<HandleList> {
    let url = `${this.url}`;
    if (typeof query !== "undefined") {
      url += `?${query}`;
    }
    const response = await this.client.get<HandleList>(url);
    return new HandleList(response.data);
  }

  async listByUser(userId: string, query?: string): Promise<HandleList> {
    let url = `${this.url}user/${userId}`;
    if (typeof query !== "undefined") {
      url += `/?${query}`;
    }
    const response = await this.client.get<HandleList>(url);
    return new HandleList(response.data);
  }
}
