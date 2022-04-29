import { IPlatformData } from "../platform/Platform.types";

export interface IGameData {
  name: string;
  platforms: IPlatformData[];
}

export interface IGame extends IGameData {}
