import APIService from '~/modules/common/API';
import { Game, GameList } from './Game';

export class GameService extends APIService {
  private url = 'games/';

  async list(): Promise<GameList> {
    const response = await this.client.get(this.url);
    return new GameList(response.data);
  }

  async ranking(): Promise<Game[]> {
    const response = await this.client.get(`${this.url}ranking/`);
    const items: Game[] = response.data;
    return items;
  }
}
