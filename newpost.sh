if [ -n "$1" ]; then
	$EDITOR _posts/`date +%Y-%m-%d-$1.markdown`
fi
