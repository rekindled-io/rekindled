import { IPagination } from "../common/Pagination";
import { IPlatformData } from "../platform/Platform.types";
import { IGame, IGameData } from "./Game.types";

export class Game implements IGame {
  name: string;
  platforms: IPlatformData[];

  constructor(data: IGameData) {
    this.name = data.name;
    this.platforms = data.platforms;
  }
}

export class GameList implements IPagination<Game[]> {
  last_page: number;
  current_page: number;
  next?: number;
  previous?: number;
  count: number;
  results?: Game[];

  constructor(data: IPagination<Game[]>) {
    this.last_page = data.last_page;
    this.current_page = data.current_page;
    this.next = data.next;
    this.previous = data.previous;
    this.count = data.count;
    this.results = data.results;
  }
}
