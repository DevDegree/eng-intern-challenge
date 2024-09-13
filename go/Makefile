build:
	@go build -tags dev -o bin/solution translator.go  

run: build
	@./bin/solution

install:
	@go get ./...
	@go mod vendor
	@go mod tidy
	@go mod download

test:
	@make
	@go clean -testcache
	@go test -v ./...