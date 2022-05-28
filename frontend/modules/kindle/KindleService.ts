import APIService from '../common/API';
import { KindleList } from './Kindle';

export class DirectKindleService extends APIService {
  private url = 'kindles/direct';

  async list(): Promise<KindleList> {
    const response = await this.client.get(this.url);
    return new KindleList(response.data);
  }
}
