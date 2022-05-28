import APIService from '../common/API';
import { NotificationList } from './Notification';

export class NotificationService extends APIService {
  private url = 'notifications/';

  async list(): Promise<NotificationList> {
    const response = await this.client.get<NotificationList>(this.url);
    return new NotificationList(response.data);
  }
}
