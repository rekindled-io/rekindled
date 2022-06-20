export function shallowFilter(list: Array<any>, item: string, key: string, value: string): Array<any> | null {
  if (item) {
    const result = list.find((o) => o[key] === item) || {};
    return Object.prototype.hasOwnProperty.call(value, result) ? result[value] : '';
  }
  return null;
}

export function deepFilter(list: Array<any>, item: string, key: string) {
  if (item) {
    const results: any[] = [];
    list.forEach((row) => {
      const found = row[key].filter((p: string) => p === item);
      if (found.length) results.push(row);
    });
    return results;
  }
}

export const buildURLQuery = (obj: object): string =>
  Object.entries(obj)
    .filter(([_, v]) => v !== '')
    .map((pair) => pair.map(encodeURIComponent).join('='))
    .join('&');
