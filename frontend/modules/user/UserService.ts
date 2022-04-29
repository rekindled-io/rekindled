import APIService from "~/modules/common/API";
import { User, UserList } from "./User";

export class UserService extends APIService {
  private url = "users/";

  async list(): Promise<UserList> {
    const response = await this.client.get<UserList>(this.url);
    return new UserList(response.data);
  }

  async retrieve(id: string): Promise<User> {
    const response = await this.client.get(`${this.url}${id}/`);
    return new User(response.data);
  }

  async create(payload: Object): Promise<User> {
    const response = await this.client.post(this.url, payload);
    return new User(response.data);
  }
}
