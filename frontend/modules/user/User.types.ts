export interface IProfileData {
  bio: string;
  location: string;
  discord_name: string;
  discord_account_number: Number;
  discord_id: string;
  steam_id: string;
}

export interface IUserData {
  username: string;
  is_true: boolean;
  last_login: Date;
  date_joined: Date;
  profile: IProfileData;
  email: string;
  original_email?: string;
  hashed_email: string;
}

export interface IUser extends IUserData {
  hasDiscord(): boolean;
}
