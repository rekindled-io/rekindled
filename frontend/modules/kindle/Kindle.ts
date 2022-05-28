import { IPagination } from '../common/Pagination';
import { IKindleData } from './Kindle.types';

export class Kindle implements IKindleData {
  source_user: string;
  source_handle: string;
  message: string;
  target_handle: string;

  constructor(data: IKindleData) {
    this.source_user = data.source_user;
    this.source_handle = data.source_handle;
    this.message = data.message;
    this.target_handle = data.target_handle;
  }

  toDataTable() {
    return {
      sourceUser: this.source_user,
      sourceHandle: this.source_handle,
      targetHandle: this.target_handle
    };
  }

  dataTableKeys() {
    return Object.keys(this.toDataTable());
  }
}

export class KindleList implements IPagination<Kindle[]> {
  last_page: number;
  current_page: number;
  next?: number;
  previous?: number;
  count: number;
  results?: Kindle[];

  constructor(data: IPagination<Kindle[]>) {
    this.last_page = data.last_page;
    this.current_page = data.current_page;
    this.next = data.next;
    this.previous = data.previous;
    this.count = data.count;
    this.results = data.results?.map((_) => new Kindle(_));
  }
}
