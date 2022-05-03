export type HandleDataTable = Pick<IHandleData, 'name' | 'game_and_platform' | 'region'>;

export type GameAndPlatform = {
  game_name: string;
  platform_name: string;
  cover: string;
  icon: string;
};

export interface IHandleData {
  id: string;
  user: string;
  game_and_platform: GameAndPlatform;
  start_period: Date;
  end_period: Date;
  name: string;
  created: Date;
  region: string;
}

export interface IHandle extends IHandleData {
  to_data_table(): HandleDataTable;
}
