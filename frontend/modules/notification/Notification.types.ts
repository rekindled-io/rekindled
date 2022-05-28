export interface INotificationData {
  recipient: string;
  timestamp: Date;
  sender: string;
  message: string;
  subject: string;
}

export interface INotification extends INotificationData {}
