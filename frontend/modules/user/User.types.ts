export interface IProfileData {
  bio: string;
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

export interface IUser extends IUserData {}
