% include('_header.tpl', title='DJ Parrot - Learn Words')
<div class="container">
	<div class="row">
		<div class="col-9">
			% include('_nav_bar.tpl')
			<textarea id="longtext" style="visibility:hidden">
				Sorry, {{ flashes[0][1] }}.
			</textarea>

			<div class="row">
				<div class="col">
					% if flashes:
						% for category, message in flashes:
						<div class="alert alert-{{ category }} alert-dismissible" role="alert" width="100%" style="margin-top: 1rem;">
							<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
							<strong>{{ category.title() }}!</strong> {{ message }}
						</div>
						% end
					% end
				</div>
			</div>

			<hr>
			<p id="statistics"></p>

		</div>
		<div class="col">
			% include('_buttons.tpl')
			% include('_controls.tpl')
			% include('_voices.tpl')
		</div>
	</div>
</div>

% include('_footer.tpl')
