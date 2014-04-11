%define		pearname	Console
%define		php_min_version 5.3.3
%include	/usr/lib/rpm/macros.php
Summary:	Symfony2 Console Component
Name:		php-symfony2-Console
Version:	2.4.3
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	http://pear.symfony.com/get/%{pearname}-%{version}.tgz
# Source0-md5:	2e07b37e61fa846b6c3c63df37883343
URL:		http://symfony.com/doc/current/components/console/index.html
BuildRequires:	php-channel(pear.symfony.com)
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php(date)
Requires:	php(json)
Requires:	php(mbstring)
Requires:	php(pcre)
Requires:	php(spl)
Requires:	php-channel(pear.symfony.com)
Requires:	php-pear >= 1.3.10
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Console component eases the creation of beautiful and testable
command line interfaces.

%prep
%pear_package_setup

# no packaging of tests
mv .%{php_pear_dir}/Symfony/Component/%{pearname}/Tests .
mv .%{php_pear_dir}/Symfony/Component/%{pearname}/phpunit.xml.dist .

# bad os
rm .%{php_pear_dir}/Symfony/Component/Console/Resources/bin/hiddeninput.exe

# fixups
mv docs/%{pearname}/Symfony/Component/%{pearname}/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT
%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md install.log
%{php_pear_dir}/.registry/.channel.*/*.reg
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
