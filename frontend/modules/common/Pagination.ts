export interface IPagination<T> {
  current_page: number;
  last_page: number;
  next?: number;
  previous?: number;
  count: number;
  results?: T;
}
