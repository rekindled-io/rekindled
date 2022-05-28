import { IPagination } from '../common/Pagination';
import { INotification, INotificationData } from './Notification.types';

export class Notification implements INotification {
  recipient: string;
  timestamp: Date;
  sender: string;
  message: string;
  subject: string;

  constructor(data: INotificationData) {
    this.recipient = data.recipient;
    this.timestamp = data.timestamp;
    this.sender = data.sender;
    this.message = data.message;
    this.subject = data.subject;
  }
}

export class NotificationList implements IPagination<Notification[]> {
  last_page: number;
  current_page: number;
  next?: number;
  previous?: number;
  count: number;
  results?: Notification[];

  constructor(data: IPagination<Notification[]>) {
    this.last_page = data.last_page;
    this.current_page = data.current_page;
    this.next = data.next;
    this.previous = data.previous;
    this.count = data.count;
    this.results = data.results;
  }
}
