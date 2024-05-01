var dagcomponentfuncs = (window.dashAgGridComponentFunctions = window.dashAgGridComponentFunctions || {});

dagcomponentfuncs.Details = function (props) {
    return React.createElement(
        'a',
        {href: '/details-view/' + props.value},
        props.value
    );
};