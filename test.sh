var1=$1
var2=$2

print_var1()
{
  echo $1
}

print_var2()
{
  echo feature/$1-dev: This is currently active. You should make all code changes related to you card here
}

if [ -z $var1 ] || { [ $var1 != "start" ] && [ $var1 != "dev" ] && [ $var1 != "qa" ] ;}
then
  print_var1 bad_val
else
  print_var2 $var1
fi
