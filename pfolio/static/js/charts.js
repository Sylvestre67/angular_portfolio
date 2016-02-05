/**
 * Created by gugs on 2/5/16.
 */
function render_cadence_chart(){
	var margin = {top: 20, right: 10, bottom: 20, left: 40},
		full_width = parseInt($('.cadence-chart').parent().width(), 10),
		width = full_width - margin.left - margin.right,
		full_height = 250,
		height = full_height - margin.top - margin.bottom,
		color_scale = ["lightBlue", "blue", "darkblue"],
		week_days = ['Sun','Mon', 'Tue','Wed','Thu','Fri','Sat'];

	var week_number = d3.time.format('%U');
	var day_of_week = d3.time.format('%w');

	var x = d3.scale.linear()
		.range([0, width]);

	var colors = d3.scale.ordinal()
    	.range(color_scale);

	var x_axis = d3.svg.axis()
		.scale(x)
		.orient("bottom")
		.tickSize(-height);

	var y = d3.scale.linear()
		.domain([0,6])
		.range([(height - 20),0]);

	var y_axis = d3.svg.axis()
		.scale(y)
		.orient('left')
		.ticks(7)
		.tickSize(10)
		.tickFormat(function(d,i){
			return week_days[i];
		});

	var graph = d3.select('.cadence-chart')
			.append('svg')
			.attr('width',full_width)
			.attr('height',full_height)
			.append('g')
				.attr('class','cadence-chart')
				.attr('transform','translate(' + margin.left + ',' + margin.top + ')');

	d3.json('static/dataset/cadence_data.json', function(error,dataset){

		if (error || dataset.length < 1){
			console.log(error);
		}else{
			var parse_date = d3.time.format('%Y-%m-%d');
			var day_number = d3.time.format('%w');
			var week_number = d3.time.format('%W');

			dataset.forEach(function(d){
				d.date = parse_date.parse(d.date);
			});

			var max_value = d3.max(dataset,function(d){ return d.value; });

			var first_week = week_number(d3.min(dataset, function(d){ return (d.date); }));
			var last_week =  week_number(d3.max(dataset, function(d){ return (d.date); }));

			x.domain([first_week,last_week]);

			colors.domain([0, max_value *.5 , max_value]);
			x_axis.ticks((last_week-first_week));

			var axis_x = graph.append('g')
				.attr('class','x axis')
				.attr('transform', 'translate(0,' + (height - margin.top) + ')')
				.call(x_axis);

			var x_legend = axis_x.append('g')
				.attr('class','x_legend')
				.attr('transform','translate(' + width + ',' + 40 + ')');

			x_legend.append('text')
				.text('weeks');

			var axis_y = graph.append('g')
				.attr('class','y axis')
				.attr('transform', 'translate(0,' + 0 + ')')
				.call(y_axis);

			//ADD EMPTY CIRCLE TO ACT LIKE A PRINT MARK IF d.value = 0
			var empty_circle = d3.selectAll('.cadence-chart .x > .tick');

			for (i = 0; i < 7 ; i++){
				empty_circle.append('circle')
					.attr('transform','translate(0,' + - (y(i)) + ')')
					.attr('r',8);
			}

			var weeks = graph.selectAll('g')
					.data(dataset)
				.enter().append('g')
					.attr('class','week')
					.attr('transform',function(d,i){
						return 'translate(' + x(week_number(d.date)) + ',' + y(day_number(d.date)) + ')'
					});

			//ADD THE VALUE CIRCLE
			weeks.append('circle')
				.attr('r',8)
				.attr('fill',function(d){ return colors(d.value); });

		}
	});
}