
CMD := ./cmd/$(NAME)
BIN := ./bin
ALL := ./...
CMDALL := $(CMD)/$(ALL)


all: build

build: clean prepare
	cd $(BIN) && \
	go build ../$(CMDALL)

run: build
	$(BIN)/$(NAME)

install: clean uninstall prepare
	go install $(CMDALL)

clean:
	go clean $(ALL)
	rm -rf bin/*

uninstall:
	go clean -i $(ALL)


prepare: vet format fix

vet:
	go vet $(ALL)

format:
	go fmt $(ALL)

fix:
	go fix $(ALL)
