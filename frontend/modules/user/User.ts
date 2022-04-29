import { IPagination } from "~/modules/common/Pagination";
import { IProfileData, IUser, IUserData } from "./User.types";

export class User implements IUser {
  username: string;
  is_true: boolean;
  last_login: Date;
  date_joined: Date;
  profile: IProfileData;
  email: string;
  original_email?: string;
  hashed_email: string;

  constructor(data: IUserData) {
    this.username = data.username;
    this.email = data.email;
    this.last_login = data.last_login;
    this.date_joined = data.date_joined;
    this.original_email = data.original_email;
    this.hashed_email = data.hashed_email;
    this.is_true = data.is_true;
    this.profile = data.profile;
  }
}

export class UserList implements IPagination<User[]> {
  last_page: number;
  current_page: number;
  next?: number;
  previous?: number;
  count: number;
  results?: User[];

  constructor(data: IPagination<User[]>) {
    this.last_page = data.last_page;
    this.current_page = data.current_page;
    this.next = data.next;
    this.previous = data.previous;
    this.count = data.count;
    this.results = data.results;
  }
}
