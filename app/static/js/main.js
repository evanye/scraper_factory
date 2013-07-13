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
    appendForm(element, type, classes);
    highlight(type, classes);
    INDEX++;
  });
});

function appendForm(element, type, classes){
  var div = $(document.createElement('div'));
  div.attr('class', 'main');

  var param_input = $(document.createElement('input'));
  param_input.attr({
    id: 'param' + INDEX,
    class: 'id',
    type: 'text'
  });

  var value_view = $(document.createElement('p'));
  value_view.attr('class', 'value');
  value_view.text(element.text().substr(0,15) + '...');

  var value_input = $(document.createElement('input'));
  var class_value = classes.length > 0 ? '|' + classes.join('|') : '';
  value_input.attr({
    id: 'value' + INDEX,
    type: 'hidden', 
    value: type + class_value,
  });

  div.append(param_input);
  div.append(value_view);
  div.append(value_input);
  div.appendTo('form');

  param_input.focus();
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