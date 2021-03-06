to_watch=$1
inotifywait -e modify,create,delete -m ${to_watch} | 
while read -r directory event filename; do 
    abs_file_path=${to_watch}/${filename}
    git -C ${to_watch} add ${abs_file_path} &
    git -C ${to_watch} commit -m "${filename} $(date +"%m.%d.%y %H:%M") ${event}" &
    git -C ${to_watch} push
done
