find . -name '*txt' -exec bash -c 'mv $0 ${0/input_/}' {} \; 
find . -name '*txt' -exec bash -c 'mv $0 ${0/output_/}' {} \; 
