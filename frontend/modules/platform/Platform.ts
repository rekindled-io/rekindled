import { IPlatform, IPlatformData } from "./Platform.types";

export class Platform implements IPlatform {
  name: string;

  constructor(data: IPlatformData) {
    this.name = data.name;
  }
}
