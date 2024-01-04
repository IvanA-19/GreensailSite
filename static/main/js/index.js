// const $newDiv = document.createElement('div');
// const $newScript1 = document.createElement('script');
// const $newScript2 = document.createElement('script')
// $newDiv.innerHTML = '<div id="vk_post_-217702747_897"></div>'
// $newScript1.type = 'type="text/javascript';
// $newScript1.src = 'https://vk.com/js/api/openapi.js?169';
// $newScript2.type = 'text/javascript'
// $newScript2.textContent = '(function() {VK.Widgets.Post("vk_post_-217702747_897", -217702747, 897, \'MzS2g7eLjM2FKdeQaqEyuQ7QqO_8\');}());';
// const $actual_events = document.querySelector('.actual');
// $actual_events.appendChild($newDiv);
// $actual_events.appendChild($newScript1);
// $actual_events.appendChild($newScript2)
const $newDiv = document.createElement('div');
const $newScript1 = document.createElement('script');
const $newScript2 = document.createElement('script')
$newDiv.innerHTML = '<div id="{{id}}"></div>'
$newScript1.type = 'type="text/javascript';
$newScript1.src = 'https://vk.com/js/api/openapi.js?169';
$newScript2.type = 'text/javascript'
$newScript2.textContent = `(function() {VK.Widgets.Post("{{id}}", -217702747, 897, \'{{hash}}\');}());`;
const $actual_events = document.querySelector('.actual');
$actual_events.appendChild($newDiv);
$actual_events.appendChild($newScript1);
$actual_events.appendChild($newScript2)