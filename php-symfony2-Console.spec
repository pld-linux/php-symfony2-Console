%define		pearname	Console
%define		php_min_version 5.3.3
%include	/usr/lib/rpm/macros.php
Summary:	Symfony2 Console Component
Name:		php-symfony2-Console
Version:	2.4.8
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/symfony/Console/archive/v%{version}/%{pearname}-%{version}.tar.gz
# Source0-md5:	334a06f0e45ebcf93e7265d08889dc3e
URL:		http://symfony.com/doc/2.4/components/console/index.html
BuildRequires:	phpab
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php(date)
Requires:	php(json)
Requires:	php(mbstring)
Requires:	php(pcre)
Requires:	php(spl)
Requires:	php-pear >= 1.3.10
Suggests:	php(posix)
Suggests:	php-symfony2-EventDispatcher
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Console component eases the creation of beautiful and testable
command line interfaces.

%prep
%setup -q -n %{pearname}-%{version}

%build
phpab -n -e '*/Tests/*' -o autoload.php .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{pearname}
cp -a *.php */ $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{pearname}
rm -r $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{pearname}/Tests
# bad os
rm $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{pearname}/Resources/bin/hiddeninput.exe

%clean
rm -rf $RPM_BUILD_ROOT
%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%dir %{php_pear_dir}/Symfony/Component/Console
%{php_pear_dir}/Symfony/Component/Console/*.php
%{php_pear_dir}/Symfony/Component/Console/Command
%{php_pear_dir}/Symfony/Component/Console/Descriptor
%{php_pear_dir}/Symfony/Component/Console/Event
%{php_pear_dir}/Symfony/Component/Console/Formatter
%{php_pear_dir}/Symfony/Component/Console/Helper
%{php_pear_dir}/Symfony/Component/Console/Input
%{php_pear_dir}/Symfony/Component/Console/Output
%{php_pear_dir}/Symfony/Component/Console/Tester
