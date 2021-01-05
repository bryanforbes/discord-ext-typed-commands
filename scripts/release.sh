#!/bin/bash

shopt -s extglob

RELEASE_VERSION="${1}"; shift
DRY_RUN_FLAG="${1}"; shift

POST_RELEASE_VERSION="${RELEASE_VERSION%%.+([[:digit:]])}.$(( ${RELEASE_VERSION##+(+([[:digit:]]).)} + 1))dev0"

DRY_RUN=0

if [[ " ${DRY_RUN_FLAG} " == " --dry-run " ]]; then
	DRY_RUN=1
fi

function execute() {
	echo "> $@"
	if [ $DRY_RUN -eq 0 ]; then
		"$@";
	fi
	return $?
}

function set_version() {
	local VERSION="${1}"; shift
	local MESSAGE="${1}"; shift

	execute poetry version "${VERSION}"
	execute git add --update pyproject.toml
	execute git commit -m "${MESSAGE}"
}

set_version "${RELEASE_VERSION}" "Release ${RELEASE_VERSION}"

execute git tag "v${RELEASE_VERSION}"

set_version "${POST_RELEASE_VERSION}" "Post release version bump"

execute git push
execute git push --tags
