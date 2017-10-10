.PHONY: unittests
unittests:
	python3 test_sound_manager.py


.PHONY: start_docker_mpd
start_docker_mpd:
	docker run --rm -d -p 6600:6600 -v $(pwd)/test_music/:/var/lib/mpd/music --name mpd vitiman/alpine-mpd:latest

.PHONY: stop_docker_mpd
stop_docker_mpd:
	docker stop mpd

.PHONY: test_suite
test_suite: start_docker_mpd unittests stop_docker_mpd