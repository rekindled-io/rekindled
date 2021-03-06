import Vue from 'vue';

Vue.filter('truncate', function (text, length, clamp) {
  clamp = clamp || '...';
  var node = document.createElement('div');
  node.innerHTML = text;
  var content = node.textContent;
  return content.length > length ? content.slice(0, length) + clamp : content;
});

Vue.filter('capitalise', function (text) {
  return text.charAt(0).toUpperCase() + text.slice(1);
});
