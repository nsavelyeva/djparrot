% include('_header.tpl', title='DJ Parrot - Login')
<div class="container">
	<div class="row">
		<div class="col-9">
			% include('_nav_bar.tpl')	
			<hr>
			<form method="POST" accept-charset="UTF-8">
				<div class="form-group row">
					<label class="col-sm-3 col-form-label" for="pitch">Username</label>
					<div class="col-sm-9">	
						<input name="username" type="text">
					</div>
				</div>
				<div class="form-group row">
					<label class="col-sm-3 col-form-label" for="pitch">Password</label>
					<div class="col-sm-9">
						<input name="password" type="password">
					</div>
				</div>
				<div class="form-group row">
					<label class="col-sm-3 col-form-label" for="pitch"></label>
					<div class="col-sm-9">
						<input value="Login" type="submit">
					</div>
				</div>
			</form>
			<hr>
			<div class="row">
				<div class="col">
					% if flashes:
						% for category, message in flashes:
						<div class="alert alert-{{ category }} alert-dismissible" role="alert" width="100%" style="margin-top: 1rem;">
							<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
							<strong>{{ category.title() }}!</strong> {{! message }}
						</div>
						% end
					% end
				</div>
			</div>
		</div>
		<div class="col">
			% include('_buttons.tpl')
			% include('_controls.tpl')
		</div>
	</div>
</div>

% include('_footer.tpl')
