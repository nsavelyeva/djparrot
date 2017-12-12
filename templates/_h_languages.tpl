<div class="row">
% for item in languages:
	<div class="form-check col">
		<label class="form-check-label">
			<input id="lang_{{ item[1] }}" name="lang_checkbox" class="form-check-input" type="checkbox" value="{{ item[1] }}"
			% if item[1] in lang_checkbox:
				checked
			% end
			>
			{{ item[2] }}
		</label>
	</div>
	% if item[1] == "el":
	<div class="w-100"></div> 
	% end
% end
</div>
