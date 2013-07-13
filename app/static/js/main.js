var CLEARED_TAGS = ['A', 'P', 'FONT', 'LI', 'PRE', 'SPAN', 'TD'];
var HIGHLIGHT_COLORS = ['#00FFFF', '#33CCCC', '#00FF00', '#FF3399'];
var INDEX = 0;

$(document).ready(function(){
  $('.view').click(function(e){
    e.preventDefault();
    var element = $(e.target);
    var type = element.get(0).tagName;

    if(CLEARED_TAGS.indexOf(type) == -1)
      return;

    var classes = getCss(element);
    appendForm(type, classes);
    highlight(type, classes);
    INDEX++;
  });
});

function appendForm(type, classes){
  $('<input>').attr({
    id: 'param' + INDEX,
    type: 'text'
  }).appendTo('form');
  $('<input>').attr({
    id: 'value' + INDEX,
    type: 'hidden',
    value: type + '|' + classes.join('|')
  }).appendTo('form');
}

function highlight(type, classes){
  var class_str = classes.length > 0 ? '.' + classes.join(' .') + ' ' : '';
  $(class_str + type).each(function(){
    $(this).css('background', HIGHLIGHT_COLORS[INDEX]);
  });
}

function getCss(element){
  var classes = [];
  var parent = element.parent();
  while(parent[0] !== $('#scraper_pageView')[0]){
    if(parent.attr('class'))
      classes.push(parent.attr('class'));
    parent = parent.parent();
  }
  return classes;
}