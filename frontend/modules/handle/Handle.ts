import { IPagination } from "../common/Pagination";
import { GameAndPlatform, IHandleData } from "./Handle.types";

export class Handle implements IHandleData {
  id: string;
  user: string;
  game_and_platform: GameAndPlatform;
  start_period: Date;
  end_period: Date;
  name: string;
  created: Date;
  region: string;

  constructor(data: IHandleData) {
    this.id = data.id;
    this.user = data.user;
    this.game_and_platform = data.game_and_platform;
    this.start_period = data.start_period;
    this.end_period = data.end_period;
    this.name = data.name;
    this.created = data.created;
    this.region = data.region;
  }

  toDataTable() {
    return {
      name: this.name,
      game: this.game_and_platform.game_name,
      platform: this.game_and_platform.platform_name,
      region: this.region,
    };
  }

  dataTableKeys() {
    return Object.keys(this.toDataTable());
  }
}

export class HandleList implements IPagination<Handle[]> {
  last_page: number;
  current_page: number;
  next?: number;
  previous?: number;
  count: number;
  results?: Handle[];

  constructor(data: IPagination<Handle[]>) {
    this.last_page = data.last_page;
    this.current_page = data.current_page;
    this.next = data.next;
    this.previous = data.previous;
    this.count = data.count;
    this.results = data.results?.map((_) => new Handle(_));
  }
}
