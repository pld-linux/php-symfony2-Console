%define		package	Console
%define		php_min_version 5.3.9
Summary:	Symfony2 Console Component
Name:		php-symfony2-Console
Version:	2.8.52
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/symfony/%{package}/archive/v%{version}/%{package}-%{version}.tar.gz
# Source0-md5:	42c08f8e3f3c00371aa80bf3d5bcc3c3
URL:		https://symfony.com/doc/2.8/components/console.htmlindex.html
BuildRequires:	phpab
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php(date)
Requires:	php(json)
Requires:	php(mbstring)
Requires:	php(pcre)
Requires:	php(spl)
Requires:	php-dirs >= 1.6
Suggests:	php(posix)
Suggests:	php-psr-Log
Suggests:	php-symfony2-EventDispatcher
Suggests:	php-symfony2-Process
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Console component eases the creation of beautiful and testable
command line interfaces.

%prep
%setup -q -n console-%{version}

%build
phpab -n -e '*/Tests/*' -o autoload.php .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}
cp -a *.php */ $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}
rm -r $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}/Tests
# bad os
rm $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}/Resources/bin/hiddeninput.exe

%clean
rm -rf $RPM_BUILD_ROOT
%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%dir %{php_data_dir}/Symfony/Component/Console
%{php_data_dir}/Symfony/Component/Console/*.php
%{php_data_dir}/Symfony/Component/Console/Command
%{php_data_dir}/Symfony/Component/Console/Descriptor
%{php_data_dir}/Symfony/Component/Console/Event
%{php_data_dir}/Symfony/Component/Console/Exception
%{php_data_dir}/Symfony/Component/Console/Formatter
%{php_data_dir}/Symfony/Component/Console/Helper
%{php_data_dir}/Symfony/Component/Console/Input
%{php_data_dir}/Symfony/Component/Console/Logger
%{php_data_dir}/Symfony/Component/Console/Output
%{php_data_dir}/Symfony/Component/Console/Question
%{php_data_dir}/Symfony/Component/Console/Style
%{php_data_dir}/Symfony/Component/Console/Tester
