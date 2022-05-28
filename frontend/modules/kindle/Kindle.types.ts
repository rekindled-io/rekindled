export interface IKindleData {
  source_user: string;
  source_handle: string;
  target_handle: string;
  message: string;
}

export interface IKindle extends IKindleData {
  to_data_table(): any;
}
