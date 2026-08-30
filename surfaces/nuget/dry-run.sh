#!/bin/sh
set -eu
dotnet run --project tests/Smoke.csproj --no-restore
